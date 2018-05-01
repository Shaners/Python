while True: # Infinite loop
    print("Tell me more...")
    more = input('> ').upper()
    if more != 'STOP':
        continue # Jump back to start
    print("Stop what?")
    polite = input('> ').upper()
    if polite == 'PLEASE':
        break # Kill infinite loop
print("How nice of you. I'll stop now.")
