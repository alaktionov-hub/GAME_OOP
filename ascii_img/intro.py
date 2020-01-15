"""
ASCII scene for game begining
"""
import time
# from ascii_img.clear_screen import clear_screen


def intro():
    '''Print ASCII scene.
    no params need
    ----------
    Returns jutp ASCII SCENE for game intro
    -------
    '''
    print(r"""
                                             ..ed$$$$$$$ee.
                                          zd$$*"".$$*$$F"**$$e.
                                        d$$"    .$$" ^$$c   ^*$$.
                                      z$$"     4$$"   ^$$c     *$b.
                                     d$P      z$$"     ^$$L     ^$$.
                                    J$P      z$$"       ^$$b     ^$$
                                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F
                                   4$$     J$$"            $$b    4$$
                                   ^$$    d$$               *$$   4$$
                                    $$L  d$$                 *$$  $$%
                                    ^$$cd$$                   *$$d$P
                                     ^$$$$                     *$$P
                                       *$$c                  .d$$"
                                        ^*$$bc.           .e$$P"
                                           ^*$$$$$$eee$$$$$*"
                                          _       __      __  _      
                                         | |      \ \    / / | |     
                                         | |     __\ \  / /__| |     
                                         | |    / _ \ \/ / _ \ |     
                                         | |___|  __/\  /  __/ |____ 
                                         |______\___| \/ \___|______|
   """)

    time.sleep(1)
    print(r"""
                   _____          __  __ ______  _____       _____ _______ _    _ _____ _____ ____  
                  / ____|   /\   |  \/  |  ____|/ ____|     / ____|__   __| |  | |  __ \_   _/ __ \ 
                 | |  __   /  \  | \  / | |__  | (___      | (___    | |  | |  | | |  | || || |  | |
                 | | |_ | / /\ \ | |\/| |  __|  \___ \      \___ \   | |  | |  | | |  | || || |  | |
                 | |__| |/ ____ \| |  | | |____ ____) |     ____) |  | |  | |__| | |__| || || |__| |
                  \_____/_/    \_\_|  |_|______|_____/     |_____/   |_|   \____/|_____/_____\____/ 

   """)
    time.sleep(2)

    print('\n'+'\n')

#   clear_screen()
    time.sleep(1)
    print(r"""
                      _____  _____   _____ ______ _   _ _______    _____          __  __ ______ 
                     |  __ \|  __ \ / ____|  ____| \ | |__   __|  / ____|   /\   |  \/  |  ____|
                     | |__) | |__) | (___ | |__  |  \| |  | |    | |  __   /  \  | \  / | |__   
                     |  ___/|  _  / \___ \|  __| | . ` |  | |    | | |_ | / /\ \ | |\/| |  __|  
                     | |    | | \ \ ____) | |____| |\  |  | |    | |__| |/ ____ \| |  | | |____ 
                     |_|    |_|  \_\_____/|______|_| \_|  |_|     \_____/_/    \_\_|  |_|______|

   """)
    print('\n')
    time.sleep(1)
    print(r"""
                                                    _______       
                                                   |__   __|      
                                             __      _| |_      __
                                             \ \ /\ / / \ \ /\ / /
                                              \ V  V /| |\ V  V / 
                                               \_/\_/ |_| \_/\_/  
                                                                 """)

    time.sleep(2)
#   clear_screen()
    print(r"""

                                       TYPE START TO DIVE INTO THE BATTLE!
                                          TYPE HELP TO SEE GAME RULES!
                                          TYPE EXIT TO FINISH GAME!
                                       TYPE SCORE TO SEE TABLE OF RESULTS!

               """)