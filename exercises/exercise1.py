print('hello world')
# 1.
# Can you make a typo that generates an error?
# Traceback (most recent call last):
  # File "C:\Users\nbw11\Desktop\School\MyRepository\Python-Fundamentals\exercises\exercise1.py", line 1, in <module>
    # prit('hello world')
# NameError: name 'prit' is not defined. Did you mean: 'print'?

# Can you make sense of the error message?
# I feel like i was able to make sense of the error message, it gave me a "did you mean?" which was cool

# Can you make a typo that doesn’t generate an error?
# I suppose you could just spell something in the message wrong.
# Why do you think it didn’t make an error?
# It wouldn't create an error because it's possible to want to display a misspelled message.

# 2.
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# 3.
message = "Hello Python Crash Course reader!"
print(message)

# You're assigning a message to a variable.

message = "Hello everybody!"
print(message)

# Was good to play with a little bit really hammer stuff home!

# 4.

def display_message():
    """display simple message"""
    print("Hello, in this chapter we are learning about creating functions!")

display_message()

def favorite_book(booktitle):
    """Display favorite book title."""
    print(f"One of my favorite books is, {booktitle.title()}!")

favorite_book('Wheel of Time')
