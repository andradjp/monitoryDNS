import lib.monitor
import lib.getdata

if __name__ == '__main__':
    g = lib.getdata
    print(g.GetData.return_data(g))
    m = lib.monitor.Monitor
    m.getDNS(m, 'jpandrade.info')