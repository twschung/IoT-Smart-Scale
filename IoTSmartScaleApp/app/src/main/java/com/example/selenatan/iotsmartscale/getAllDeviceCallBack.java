package com.example.selenatan.iotsmartscale;

import java.util.ArrayList;

/**
 * Created by Terry on 24/1/16.
 */
interface getAllDeviceCallBack {
    public abstract void done(ArrayList<Device> returnedDevices);
}