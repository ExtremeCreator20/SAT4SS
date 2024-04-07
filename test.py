import ctypes

def toggle_airplane_mode():
    # Define the GUID for the network connections
    GUID_DEVINTERFACE_LIST = "{4D36E972-E325-11CE-BFC1-08002BE10318}"

    # Load SetupAPI
    setupapi = ctypes.windll.LoadLibrary("SetupAPI")

    # Call SetupDiGetClassDevs to get device info set for network adapters
    hDevInfo = setupapi.SetupDiGetClassDevsW(None, GUID_DEVINTERFACE_LIST, None, 0x00000002)

    if hDevInfo:
        # Toggle airplane mode by enabling or disabling network adapters
        for i in range(256):
            devinfo_data = ctypes.create_string_buffer(2048)
            devinfo_data_size = ctypes.c_ulong(ctypes.sizeof(devinfo_data))

            # Get device info data for network adapter
            success = setupapi.SetupDiEnumDeviceInfo(hDevInfo, i, ctypes.byref(devinfo_data))
            if not success:
                break

            # Get device instance ID
            devinst_id = ctypes.create_unicode_buffer(255)
            if setupapi.CM_Get_Device_IDW(devinfo_data, devinst_id, 255, 0) == 0:
                # Enable or disable network adapter
                setupapi.CM_Locate_DevNodeW(None, ctypes.byref(devinst_id), 0)
                setupapi.CM_Request_Device_EjectW(devinst_id, None, None, 0, 0)

    # Cleanup device info set
    setupapi.SetupDiDestroyDeviceInfoList(hDevInfo)

# Toggle airplane mode
toggle_airplane_mode()
