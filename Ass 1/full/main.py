import host

if __name__ == "__main__":
    
    my_host = host.Host(42069, 1, 0.5, 5000)
    my_host.addClients(100)

    for i in range(1000):
        my_host.Step()
    my_host.Plot(0, 1)