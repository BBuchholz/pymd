def list_config():
  print("")
  print("Listing Config:")
  print("default folder is: [folder name goes here]")
  print("Finished Listing Config")
  print("")

def menu():
  """Display the menu and get the user's choice."""
  print("")
  print("Welcome to tha MyriaD MarkDown Matrix (MDMDM)")
  print("")
  print("please select an option:")
  print("List Config (lc)")
  print("List Files (lf)")
  print("Quit (q)")
  choice = input("Enter your choice: ")
  return choice

def list_files():
  print("")
  print("Listing Files")
  print("files for default folder should be displayed here")
  print("Finished listing files")
  print("")

def main():
  """Run the main loop."""
  while True:
    choice = menu()
    if choice == "lc":
      list_config()
    elif choice == "lf":
      list_files()
    elif choice == "q":
      break
    else:
      print("")
      print("I'm sorry, I didn't understand, ")
      print("please try again")
      print("")

if __name__ == "__main__":
  main()