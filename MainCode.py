#Treasure Island game as the movie : Treasure planet
user_name = input("To start the game please enter last name ")
print('''  ..;===+.
                                                                  .:=iiiiii=+=
                                                               .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                         .=i==))))ii)))I:i++
                                                       +)+))iiiiiiii))I=i+:'
                                  .,:;;++++++;:,.       )iii+:::;iii))+i='
                               .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                             ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                           ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                          ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                       ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                      ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                      =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                     +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                     =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                  +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
               =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
             +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
           :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
         .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
       +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
     .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
   .+=i:)))))))=+ii+
  .;==i+::::=)i=;
  ,+==iiiiii+,
  `+=+++;`
  ''')
user_input1 = input(f"Welcome to Treasure planet!.\nCaptain {user_name}. The Cyborg crew found us.\nWe must flee! which way do you choose, right or left? ").lower()
if user_input1 == "right":
    print("HO NO! the Cyborg's crew caught us! \nGAME OVER. ")
elif user_input1 == "left" :
    print("""                             o         .                       .
                .               0                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
                             O        .             +     .
         .              .   *              .           .
       +        .
                 .        o                   ,                ,    ,
 .                                               .
      .          ,      /                                     +
   .          .     .  /              .                   .            .
     .          ,,,  ,o          ,             .                .
              #*#,  #/#,,  .                              .        .
            ##*#,  #/##,#               .                        .
   .       ##*#,  #O##,#*#                +     .                     ,
        .    #,  #/##,#*##              .                     .
      .     \   #%##,#*##         .                             ,       .
          .   _ /      /.   .                    .             .          ,
  ,            /   -             .                         .
____^/\___^--_O__/\_____-^^-^--_______/\/\---/\___________---______________
   /\^ ~~ ^ ~~ ^ ~~~~ ^ ~~~~~ ^/\        ^^ ^  '\ ^     ~~~     ^       ~~~
         --       ~~ ~~            ~~  ~      ~         ~~~  __       ^
   --  ~~                     ~~~--  ^  ^           ^^ ^   ^ ~__   ~~  __ ~
    """)
    user_input2 = input(f"Great job captain {user_name}! you successfully escape the Cyborg but you crashed your spaceship near  a mistery swomp.\nDo you want siwm or wait ? ").lower()
    if user_input2 == "swim":
        print("HO NO!you have been Attacked by a poisionos space fish, Game Over.")
    elif user_input2 == "wait":
        print('''   ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
        ''')
        user_input3 = input(f"""Great you have waited for long time and a rescue boat has arrived and leads you to three strange doors.
         Captain {user_name} which door do you choose:? blue, red or yellow? """).lower()
        if user_input3 == "red":
             print("You have been burned by fire.\nGame over.")
        elif user_input3 == "blue":
            print("You have been eaten by wild beasts.\nGmae over.")
        elif user_input3 == "yellow":
            print("""        _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           '.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\h||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\h/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
            """)
            print("You did it! you have found the treasure!\nYou win! ")
        else:
            print("GAME OVER")

    else:
        print("Please choose Swim or wait")

else:
    print("Please choose right or left")
