import sys
#sys.path.append('..\pylib')
sys.path.append('/home/pi/pylib')

from terminal_font import TerminalFont
from app_config import app

class Starter():

    def __connect_to_mqtt_broker(self):
        broker = app.server.mqtt.broker_addr
        port = app.server.mqtt.port
        uid = app.server.mqtt.username
        password = app.server.mqtt.password
        g_mqtt.connect_broker(broker, port, uid, password)

    def __init__(self):
        self.__connect_to_mqtt_broker()
        
        self.__YELLOW = TerminalFont.Color.Fore.yellow
        self.__GREEN = TerminalFont.Color.Fore.yellow
        self.__RESET = TerminalFont.Color.Control.reset

        # subscribe all topics from config files
        topic_count = 0
        for topic in app.server.mqtt.subscript_topics.topic_dict.keys():
            g_mqtt.subscribe(topic)
            topic_count += 1
            print('Setting app from MQTT:  sid= %i, topic= %s' %(topic_count,topic))


        print('MQTT subscription is done')

        print(self.__YELLOW + TerminalFont.Color.Background.blue)
        print('System is initialized. Now is working')
        print(self.__RESET)

    pass

def show_welcome():
    welcome=[]
    welcome.append('                                                           ')
    welcome.append('     (\ (\                                                 ')
    welcome.append('  *  ( -.-)   * * * * * * * * * * * * * * * * *            ')
    welcome.append('  *  O_(")(")                                    *         ')
    welcome.append('  *                 Go game AI and Robot            *      ')
    welcome.append('  *                     Version 0.38                  *    ')
    welcome.append('  *                                                     *  ')
    welcome.append('  *     Copyright @2020 Shandong Perfect PTE.LTD.       *  ')
    welcome.append('  *           http://voicevon.vicp.io:7005              *  ')
    welcome.append('  *                                                     *  ')
    welcome.append('  *                                                     *  ')
    welcome.append('  *                System is loading...                 *  ')
    welcome.append('  *                                                     *  ')
    welcome.append('  * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ')
    welcome.append('                                                           ')

    for w in welcome:
        print('                      ' + TerminalFont.Color.Control.bold + TerminalFont.Color.Fore.yellow + TerminalFont.Color.Background.blue + w + TerminalFont.Color.Control.reset)
    print(TerminalFont.Color.Control.reset)



if __name__ == "__main__":
    show_welcome()
    from mqtt_helper import g_mqtt
    my_starter = Starter()




