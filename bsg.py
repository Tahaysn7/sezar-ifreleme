def Brute(Text):
    DecryptText = ""
    Key = 1 
    alfabe=['a','b' ,'c' ,'ç', 'd', 'e', 'f', 'g' ,'ğ' , 'h' ,'ı' , 'i' ,'j','k' ,'l' ,'m' ,'n' ,'o' ,'ö' , 'p' ,'r' ,'s' ,'ş','t' ,'u' ,'ü', 'v', 'y' ,'z']
    while Key < 29:
        for i in Text:


        #DecryptText+=alfabe[(alfabe.index(i)+3)%len(alfabe)]
         # DecryptText = "'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı','i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z' "
            DecryptText = DecryptText + chr(ord(i) - Key)
        print("[+] Key>>",str(Key) + " Decrypt Text>>",DecryptText)
        Key += 1
        DecryptText = ""


print("""

[01] Şifreyi Çöz
[9] Exit
""")

Option = int(input("Option>> "))
if Option == 9:
    print("[-] Exit...")
    exit

elif Option == 1:
    Text = input("[+] Text>> ")
    Brute(Text)
else:
    print("[?] Please Select Options !")
    exit