from cs_gamestate.endpoint import GSIServer
import websocket, json

def main() -> None:
    """
    Main function
    """
    # Run forever

    ip = input("控制器IP地址: ")
    url = f"ws://{ip}:60536/1"
    ws = websocket.WebSocket()
    ws.connect(url)
    print("Connected to controller")

    ws.send(json.dumps({
        "cmd": "set_pattern",
        "pattern_name": "经典",
        "intensity": 15,
        "ticks": 0
    }))

    GSI = GSIServer('/gsi', 55420)
    health = 100

    while True:
        try:
            # Read game state
            state = GSI.read(block=True)
            # Print game state
            # print(state.player)

            if state.player is not None:
                if state.player.state is not None:
                    if state.player.state.health is not None:
                        if state.player.state.health != health:
                            print("Player health changed to:", state.player.state.health)
                            if state.player.state.health < health:
                                print("Player took damage")
                                ws.send(json.dumps({
                                    "cmd": "set_pattern",
                                    "pattern_name": "经典",
                                    "intensity": 100,
                                    "ticks": 0
                                }))
                            health = state.player.state.health
        except ConnectionAbortedError:
            print("Connection aborted")
            break

if __name__ == '__main__':
    main()
