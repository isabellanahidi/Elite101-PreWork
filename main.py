
def printOptions():
  print("1. ")
  print("2. ")
  print("3. ")
  print("4. Exit the Conversation")

def getInput():
  userInput = input("Enter your choice: ")
  return userInput
  
def main():
  print('Welcome to the Elite 101 Chatbot!')
  userName = input('What is your name? ')
  userAge = input('Nice to meet you ' +  userName + '! How old are you? ')
  
  print('Welcome ' + userName + '! Being ' + userAge + ' is a great age!')
  print('How can I help you today?')
  printOptions()
  userInput = getInput()
  if userInput == '4':
    print('Thank you for using the Elite 101 Chatbot! Have a great day!')
  elif userInput == '3':
    print('You picked 3')
  elif userInput == '2':
    print('You picked 2')
  elif userInput == '1':
    print('You picked 1')


main()
