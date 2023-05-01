#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import pyaudio
import speech_recognition as sr
from transformers import BertTokenizer
import torch
import numpy as np
import re

def publisher_node():
	rospy.init_node('publisher_node')
	pub = rospy.Publisher('my_topic', String, queue_size=10)
	rate = rospy.Rate(0.1) # Hz

	while not rospy.is_shutdown():
		r = sr.Recognizer()
		text=""
		with sr.Microphone() as source:
    			print("Speak Anything :")
    			audio = r.listen(source)
    			try:
        			text = r.recognize_google(audio)
        			print("You said : {}".format(text))
    			except:
        			print("Sorry could not recognize what you said")
        			continue
		rospy.loginfo("Publishing message: %s", text)

		model = torch.load('./trained_model_copy',map_location=torch.device('cpu'))
		model.eval()

		# Apply the tokenizer
		#sentence = "Set the max velocity to 10"
		tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
		#test_ids, test_attention_mask = tokenize_and_format(text)
		#test_ids = test_ids[0]
		#test_attention_mask = test_attention_mask[0]

		encoding = tokenizer(text, return_tensors="pt")
		test_ids = []
		test_attention_mask = []

		test_ids.append(encoding['input_ids'])
		test_attention_mask.append(encoding['attention_mask'])
		test_ids = torch.cat(test_ids, dim = 0)
		test_attention_mask = torch.cat(test_attention_mask, dim = 0)

		device = torch.device('cpu')

		with torch.no_grad():
  			output = model(test_ids.to(device), token_type_ids = None, attention_mask = test_attention_mask.to(device))

		prediction = np.argmax(output.logits.cpu().numpy()).flatten().item()
		prediction += 2
		if(prediction == 15):
			prediction = 1
		rospy.loginfo("Predicted Label: " + str(prediction))
		number2 = -1
		if prediction >= 7:
    			number = re.search(r'\d+(?:.\d+)?', text)
    			if number:
        			number2 = float(number.group())
    			else:
        			print("No number found in the string.")

		# Model class must be defined somewhere
		pub.publish(str(prediction) + "," + str(number2))
		rate.sleep()

def tokenize_and_format(sentences):
  tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

  # Tokenize all of the sentences and map the tokens to thier word IDs.
  input_ids = []
  attention_masks = []

  # For every sentence...
  for sentence in sentences:
      # `encode_plus` will:
      #   (1) Tokenize the sentence.
      #   (2) Prepend the `[CLS]` token to the start.
      #   (3) Append the `[SEP]` token to the end.
      #   (4) Map tokens to their IDs.
      #   (5) Pad or truncate the sentence to `max_length`
      #   (6) Create attention masks for [PAD] tokens.
      encoded_dict = tokenizer.encode_plus(
                          sentence,                      # Sentence to encode.
                          add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                          max_length = 64,           # Pad & truncate all sentences.
                          padding = 'max_length',
                          truncation = True,
                          return_attention_mask = True,   # Construct attn. masks.
                          return_tensors = 'pt',     # Return pytorch tensors.
                    )

      # Add the encoded sentence to the list.
      input_ids.append(encoded_dict['input_ids'])

      # And its attention mask (simply differentiates padding from non-padding).
      attention_masks.append(encoded_dict['attention_mask'])
  return input_ids, attention_masks


if __name__ == '__main__':
	try:
		publisher_node()
	except rospy.ROSInterruptException:
		pass
