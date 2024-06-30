const path = require('path');
const url = require('url');
const {app, BrowserWindow} = require('electron');

let win;

function creatWindow() {
    win = new BrowserWindow({
        width: 700, 
        height: 500,
        frame: null,
        transparent: true,
        icon: __dirname + "/img/icon.png",
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true,
        },
    });


    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));

    win.webContents.openDevTools();

    win.on('closed', () => {
        win = null;
    });
}

app.on('ready', creatWindow);

app.on('window-all-closed', () => {
    app.quit();
});
