class ExampleClass():
    # This function, __init__, is called any time a copy of this class is created
    # This sets up the class variables for us. 
    # Anytime you see "self.something = something", that's one of the class's variables
    def __init__(self, name, level, date, time): #all variables listed on this line, other than self, MUST be provided
        self.name = name 
        self.level = level
        self.date = date
        self.time = time

    # This is called a "Getter" function. 
        # It "gets" the information of one of the class variables
        # Then returns it to whatever called the function
    def getLevel(self):
        return self.level
    
    # This is called a "Setter" function
        # It "sets" new information for one of the class variables
        # It does not return any information
    def setLevel(self, newLevel):
        self.level = newLevel

    # Typically, there will be one "getter" and one "setter" for every variable that other files use.
    
    def getDate(self):
        return self.date
    def setDate(self, newDate):
        self.date = newDate

    def getTime(self):
        return self.time
    def setTime(self, newTime):
        self.time = newTime

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName

    def exampleClassFunction(self):
        print("Hello from example class function! A function in a class!")

def exampleFunction():
    print("Hello from example function! This function belongs to the whole file, not a specific class!")

def exampleFunctionWithUntypedParameters(message, number): #parameters are the variables inside of these parentheses (these things)
    print("This example function can only be called if you provide one variable per parameter")
    print("The parameters don't have to be a specific type. Many different kinds might work!")
    print(message)
    print(str(number))

def exampleFunctionWithTypedParameters(message: str, number: int):
    print("This example function can only be called if you provide a variable for every parameter AND they are the right type.")
    print("The function will crash when called if you use the wrong number of variables or the wrong data types for them.")
    print(message)
    print(str(number))

def everythingTogether():
    # This is how you create a variable
    variableName = "new data"
    variableName2 = 1

    # This is how you create a list
    variableList = [variableName, variableName2]

    # This is how you loop through a list
    for item in variableList:
        print(str(item)) # "item" is whatever item is at the current part of the list.

    # This is how you create a copy of a class
    myClass = ExampleClass("Level 5 Team", 5, "Tuesday", "8PM EST")

    # Different copies have different information
    mySecondClass = ExampleClass("Little Coders", 0, "Monday", "4PM EST")
    
    # This is how you access information stored in a class variable
    info = myClass.level # this stores the information in the new variable, "info"
    data = mySecondClass.name # same thing, but in the new variable, "data"

    # This is how you change information stored in a class variable
    myClass.time = "9PM EST"
    mySecondClass.name = "Little Coders++"

    # This is how you use getter and setter methods to access and change information (industry standard):
    myClass.setLevel(10)
    infoTwo = myClass.getLevel()

    mySecondClass.setDate("Sunday")
    dataTwo = myClass.getDate()

    # This is how you call a function that is part of a class
    myClass.exampleClassFunction()
    mySecondClass.exampleClassFunction()

    # This is how you call a function with no parameters
    exampleFunction()

    # This is how you call a function with parameters
    exampleFunctionWithUntypedParameters(data, info)
    exampleFunctionWithTypedParameters(dataTwo, infoTwo)