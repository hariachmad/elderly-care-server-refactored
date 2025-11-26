from application.modules.cor.BlackListHandler import BlackListHandler
from application.modules.cor.InferenceHandler import InferenceHandler
from application.modules.cor.PageNavigatorHandler import PageNavigatorHandler


userInput = "where is my medicine schedule?"

blacklist = BlackListHandler()
inference = InferenceHandler()
pageNavigator = PageNavigatorHandler()
blacklist.set_next(inference).set_next(pageNavigator)

result = blacklist.handle(userInput)

print(result)
