def convert_length():
    value=float(input("enter length in meters:"))
    print(f"{value}meters={value*100})centimeters")
    print(f"{value}meters={value*3.208084}feet")


    def convert_weight():
        value=float(input("enter weight in kilograms:"))
        print(f"{value}kilograms={value*1000}grams")
        print(f"{value}kilograms={value*2.20462}ponds")

        def convert_temperature():
            value=float(input("enter temperature in celcius"))
            print(f"{value}C={value*9/5+32}F")


            def main():
                print("simple unit convertor")
                while true:
                    print("\nchoose convertion type:")
                    print("1. length(meters to centimeter and feet)")
                    print("2.weight(kilograms to grams and ponds)")
                    print("3.temperature(celcius to fahrenheight)")
                    print("4.exit")

                    choice=input("enter your choice(1-4):")
                    if choice== '1':
                        convert_length()
                        elif choice=='2':
                            convert_weight()
                            elif choice=='3':
                                convert_temperature()
                                elif choice=='4':
                                    print("exiting the convertor.goodbye!")
                                    break
                                    else:
                                        print("invalid choice,please try again")
                                        if___name___=="__main__":
                                            main()


                            
