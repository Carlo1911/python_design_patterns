from singleton_object import SingletonObject

logger = SingletonObject('/Users/calva/Proyectos/Patrones/Singleton/filename.log')

logger.info("This is an info message for singleton logger")

print(logger)

logger = SingletonObject('/Users/calva/Proyectos/Patrones/Singleton/filename2.log')

logger.info("This is an info message for singleton logger")

print(logger)
