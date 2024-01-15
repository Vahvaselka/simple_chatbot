import string
import random
import loggning

positiva = ["Berätta mer", "Jag förstår...", "Ahaa...", "Jag lyssnar..."] #listar olika svar för positiva fall
negativa = ["Varför är du på så dåligt humör?", "varför inte", "Är det sant?", "Är du helt säker?", "Inte det?"] # listar olika svar för negativa fall
familj = ["Är din bror likadan?", "Berätta mer om din familj", "Hur är din relation med dina föräldrar?" ] # listar svar om det handlar om familj
avslutnings_lista=['Hejdå', 'hejs svejs', 'sluta', 'stopp', 'gonatt', 'god natt'] # listar alternativ för att sluta

def main():
    print("**************************************************")
    print()
    print(" Välkommen till Elizas mottagning ")
    print()
    print("**************************************************")
    print()
    print('(Du kan sluta när som helst genom att svara\n "Hejs svejs" , "Hejdå", "sluta", "stopp", "gonatt" eller "god natt")')
    print()
    print('Berätta för mig om dina problem...')

    while True: #kollar när det är dags att sluta samt loggar svar
        anvandarens_text= input("\n> ").lower() # byter användares text till lilla bokstav
        loggning.log(anvandarens_text) # loggar svaret till ett annat fil
        svar=svara(anvandarens_text) # anropar funktionen som ansvar för vad eliza svarar
        if svar==0:
            print('Tack för besöket. Betala in 150 EUR på mitt konto.')
            break
        else:
            print(svar)
            loggning.log(svar)


def svara(text): # funktionen som ansvar för vad eliza svarar
        if text in avslutnings_lista: # kollar om användaren vill avsluta
            return 0
        text=text.replace('!','') #tar bort alla specialtecken ur anvandarens text, svaret sätter ändå ett frågetecken i slutet.
        text=text.replace('?','')
        text=text.replace('.','')
        text=text.replace(':','')
        text=text.replace(';','')
        urspr_ord = str.split(text) #Dela upp användarens mening i en lista av ord
        nya_ord = urspr_ord[ : ] #Skapa en ny lista som innehåller samma ord (en kopia)
        for i in range(len(urspr_ord)): # går igenom alla ord ett åt gången.
            if urspr_ord[i] == "jag": # byter från första till andra person
                nya_ord[i] = "du"
            if urspr_ord[i] == "mig":
                nya_ord[i] = "dig"
            elif urspr_ord[i] == "min":
                nya_ord[i] = "din"
            elif urspr_ord[i] == "mitt":
                nya_ord[i] = "ditt"
            elif urspr_ord[i] == "mina":
                nya_ord[i] = "dina "
            elif urspr_ord[i] == "du": #byter från andra första person
                nya_ord[i] = "jag"
            elif urspr_ord[i] == "dig":
                nya_ord[i] = "mig"
            elif urspr_ord[i] == "din":
                nya_ord[i] = "min"
            elif urspr_ord[i] == "ditt":
                nya_ord[i] = "mitt "
            elif urspr_ord[i] == "dina":
                nya_ord[i] = "mina"
        if "pappa"in urspr_ord or "mamma" in urspr_ord: # kollar om saken handlar om familj
            return(random.choice(familj))
        elif "nej" in urspr_ord or "aldrig" in urspr_ord: # kollar om saken behövs ett negativ svar
            return(random.choice(negativa))
        elif nya_ord == urspr_ord: # kollar om det behövs positivs svar
            return(random.choice(positiva)) 
        else:
             return(" ".join(nya_ord)+'?') #Slå ihop alla ord i nya_ord-listan till en sträng och skriv ut den. \n samt lägger till en frågatecken
main()