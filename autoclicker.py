import pyautogui
from time import sleep
import pyperclip

class AutoSenderEmail:
	def __init__(self, delay_on_seconds, subject, message):
		self.delay_on_seconds = delay_on_seconds
		self.subject = subject
		self.message = message
		self.pos_x = 0
		self.pos_y = 0
		self.list_emails = list()
		

	def set_position_redact_button(self, pos_x, pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y

	def set_emails_by_file(self, file_name):
		with open(file_name) as file:
			for line in file:
				self.list_emails.append(line.strip())

	def move_cursor_with_delay(self, x, y):
		pyautogui.moveTo(x, y)
		sleep(self.delay_on_seconds)

	def move_to_redact_button(self):
		self.move_cursor_with_delay(self.pos_x, self.pos_y)

	def click_with_delay(self):
		pyautogui.click()
		sleep(self.delay_on_seconds)

	def copy_text_with_delay(self, text_to_copy):
		pyperclip.copy(text_to_copy)
		sleep(self.delay_on_seconds)

	def hotkey_doble_with_delay(self, first_key, second_key):
		pyautogui.hotkey(first_key, second_key)
		sleep(self.delay_on_seconds)

	def copy_and_paste(self, text):
		self.copy_text_with_delay(text)
		self.hotkey_doble_with_delay('command', 'v')

	def hotkey_single_with_delay(self, key):
		pyautogui.hotkey(key)
		sleep(self.delay_on_seconds)

	def run_auto_sender_for_mac(self):
		self.move_to_redact_button()
		self.click_with_delay()

		for email in self.list_emails:
			self.move_to_redact_button()
			self.click_with_delay()
			self.copy_and_paste(email)
			self.hotkey_single_with_delay('tab')
			self.copy_and_paste(self.subject)
			self.hotkey_single_with_delay('tab')
			self.copy_and_paste(self.message)
			self.hotkey_single_with_delay('tab')
			self.hotkey_single_with_delay('enter')



subject_string = "example subject"

message_string = """example message"""

sender_object = AutoSenderEmail(delay_on_seconds = 0.1, 
							  subject = subject_string, 
							  message = message_string)

sender_object.set_position_redact_button(1047, 290)

sender_object.set_emails_by_file('emails.txt')
sender_object.run_auto_sender_for_mac()




