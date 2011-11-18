import TraktForBoxee

if __name__ == '__main__':
    client = bbc.BoxeeBoxClient("666", "192.168.1.148", 9090, "unittest", "Unit Testing Harness")
    #while(true)
    #test = self.client.callMethod("GUI.NotificationShow", {'msg': "Testing notifications..."}, True)
    #print client.callMethod("GUI.NotificationShow", {'msg': 'Scrobbling to Trakt...'}, True)
    #time.sleep(3)
    #print client.callMethod("GUI.NotificationShow", {'msg': 'Scrobbled!'}, True)
    #print client.callMethod("Player.GetActivePlayers")
    #print client.callMethod("VideoPlayer.GetPercentage")
    t = client.callMethod("System.GetInfoLabels", {'labels': ['VideoPlayer.Title', 'VideoPlayer.TVShowTitle', 'VideoPlayer.Season', 'VideoPlayer.Time', 'VideoPlayer.Year']}, True);
    print t["result"];
    #t = client.callMethod("System.GetInfoBooleans", {'booleans': ["system.IdleTime(300)"]}, True);