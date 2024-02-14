array = [];
  def prompt():
      x = input("Enter an integer number (blank to exit): ");

      if(x != ""):
          array.append(int(x));
          prompt();
      else:
          print(f"Data: {array}");

  prompt();
