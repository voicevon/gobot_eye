from app_config import app
import sys
from app_global.color_print import CONST
sys.path.append('../pylib')
import mqtt_helper

class Starter():

    def __connect_to_mqtt_broker(self):
        broker = app_config.server.mqtt.broker_addr
        port = app_config.server.mqtt.port
        uid = app_config.server.mqtt.username
        password = app_config.server.mqtt.password
        g_mqtt.connect_broker(broker, port, uid, password)

    def __init__(self):
        self.__connect_to_mqtt_broker()
        # self.__eye = RobotEye()
        self.__robot_sower = RobotSower()

        self.__goto = self.__on_state_begin
        self.__system_turn_on = True

        self.__YELLOW = TerminalFont.Color.Fore.yellow
        self.__GREEN = TerminalFont.Color.Fore.yellow
        self.__RESET = TerminalFont.Color.Control.reset

        # subscribe all topics from config files
        topic_count = 0
        for topic in AppConfig.server.mqtt.subscript_topics.topic_dict.keys():
            g_mqtt.subscribe(topic)
            topic_count += 1
            print('subscribed MQTT topics from config :  %i, %s' %(topic_count,topic))


        print('MQTT subscription is done')

        print(self.__YELLOW + TerminalFont.Color.Background.blue)
        print('System is initialized. Now is working')
        print(self.__RESET)

        self.__robot_sower.start()
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
        print('                      ' + CONST.print_color.control.bold + CONST.print_color.fore.yellow + CONST.print_color.background.blue + w + CONST.print_color.control.reset)
    print(CONST.print_color.control.reset)



if __name__ == "__main__":
    show_welcome()
    my_starter = Starter()




