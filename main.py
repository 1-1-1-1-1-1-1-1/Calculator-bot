import asyncio
import re
from time import sleep

from telethon import events

from config import bot


# === Define handlers =========================================================


@bot.on(events.NewMessage(pattern=""))
async def handler(event):
	text = event.text
	text = text.rstrip('.')

	math_signs = "-+*/"  # `-` should be first (or last)
	spaces = " \t\f\n"
	numbers = r'\d'
	brackets = '()'
	dot = '.'  # for float numbers

	all_allowed_symbols = (
		math_signs,
		spaces,
		numbers,
		brackets,
		dot
	)
	all_allowed_symbols = ''.join(all_allowed_symbols)

	if '-' in all_allowed_symbols:
		# minus sign should be first, only first.
		assert '-' not in all_allowed_symbols[1:]

	try:
		if re.fullmatch('[' + all_allowed_symbols + ']+', text):
			if re.search('[' + math_signs + ']', text):
				# Case is not trivial as count is required, considired
				result = eval(text)
	except:
		pass

	if 'result' not in locals():
		return

	# Otherwise the result was counted.

	if re.sub(r'\s', '', text) == '1000-7':
		chat = event.chat.id

		await bot.send_file(chat, 'media/triggered.png',
			reply_to=event.reply_to_msg_id)

		# Sleep for a while.
		sleep(3)

		_data = [1000]
		prev = _data[0]
		while True:
			maybe_next = prev - 7
			if maybe_next >= 0:
				_data.append(maybe_next)
				prev = maybe_next
			else:
				# Always occures after a finite sequence iterations.
				break
		data = map(str, _data)
		msg = '\n'.join(data)
		await event.reply(msg)

		try:
			# Leave the chat.
			await bot.kick_participant(chat, 'me')
		except:
			# Can occur when chat is private.
			pass
	else:
		result = str(result)
		await event.reply(result)


def main():
	"""Run the bot."""
	print("Running main...")
	asyncio.run(bot.run_until_disconnected())


if __name__ == '__main__':
	main()
