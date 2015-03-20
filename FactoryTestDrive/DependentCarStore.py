# from FactoryTestDrive.cheapFreCar import cheapFreCar
# from FactoryTestDrive.cheapJpCar import cheapJpCar
# from FactoryTestDrive.cheapUsCar import cheapUsCar
# from FactoryTestDrive.exGerCar import exGerCar
# from FactoryTestDrive.exItaCar import exItaCar
#
#
# class DependentCarStore(object):
#     def createCar(self, type, style):
#         if style == "EX":
#             if type == "GER":
#                 car = exGerCar()
#             elif type == "ITA":
#                 car = exItaCar()
#         elif style == "CHEAP":
#             if type == "US":
#                 car = cheapUsCar()
#             elif type == "JP":
#                 car =cheapJpCar()
#             elif type == "FRE":
#                 car = cheapFreCar()
#         else:
#             raise TypeError("No such car type: " + type)
#
#         car.construct()
#         car.wash()
#         car.dry()
#         car.ship()
#         return car