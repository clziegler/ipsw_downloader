#!/usr/bin/env python
# -*- coding: utf-8 -*-

iPhones = {
    "iPhone 7": [
        ("iPhone9,1", "iPhone_7"),
        ("iPhone9,2", "iPhone_7_Plus"),
        ("iPhone9,3", "iPhone_7"),
        ("iPhone9,4", "iPhone_7_Plus"),
    ],
    "iPhone 8": [
        ("iPhone10,1", "iPhone_8"),
        ("iPhone10,2", "iPhone_8_Plus"),
        ("iPhone10,4", "iPhone_8"),
        ("iPhone10,5", "iPhone_8_Plus"),
    ],
    "iPhone X": [("iPhone10,3", "iPhone_X_Global"), ("iPhone10,6", "iPhone_X_GSM"),],
    "iPhone XS": [
        ("iPhone11,2", "iPhone_XS"),
        ("iPhone11,4", "iPhone_XS_Max"),
        ("iPhone11,6", "iPhone_XS_Max_Global"),
    ],
    "iPhone XR": [("iPhone11,8", "iPhone_XR"),],
    "iPhone 11": [
        ("iPhone12,1", "iPhone_11"),
        ("iPhone12,3", "iPhone_11_Pro"),
        ("iPhone12,5", "iPhone_11_Pro_Max"),
    ],
    "iPhone SE": [("iPhone12,8", "iPhone_SE_2nd_Gen"),],
}


iPads = {
    "iPad Mini 4": [("iPad5,2", "4th Gen iPad mini (WiFi+Cellular)"),],
    "iPadair_2": [
        ("iPad5,3", "iPad Air 2 (WiFi)"),
        ("iPad5,4", "iPad Air 2 (Cellular)"),
    ],
    "iPad_pro": [
        ("iPad6,3", "iPad Pro (9.7 inch, WiFi)"),
        ("iPad6,4", "iPad Pro (9.7 inch, WiFi+LTE)"),
        ("iPad6,7", "iPad Pro (12.9 inch, WiFi)"),
        ("iPad6,8", "iPad Pro (12.9 inch, WiFi+LTE)"),
    ],
    "iPad_2017": [("iPad6,11", "iPad (2017)"), ("iPad6,12", "iPad (2017)"),],
    "iPad_pro_2nd_gen": [
        ("iPad7,1", "iPad Pro 2nd Gen (WiFi)"),
        ("iPad7,2", "iPad Pro 2nd Gen (WiFi+Cellular)"),
        ("iPad7,3", "iPad Pro 10.5-inch"),
        ("iPad7,4", "iPad Pro 10.5-inch"),
    ],
    "iPad_6th_gen": [
        ("iPad7,5", "iPad 6th Gen (WiFi)"),
        ("iPad7,6", "iPad 6th Gen (WiFi+Cellular)"),
    ],
    "iPad_7th_gen": [
        ("iPad7,11", "iPad 7th Gen 10.2-inch (WiFi)"),
        ("iPad7,12", "iPad 7th Gen 10.2-inch (WiFi+Cellular)"),
    ],
    "iPad_pro_11in": [
        ("iPad8,1", "iPad Pro 11 inch (WiFi)"),
        ("iPad8,2", "iPad Pro 11 inch (1TB, WiFi)"),
        ("iPad8,3", "iPad Pro 11 inch (WiFi+Cellular)"),
        ("iPad8,4", "iPad Pro 11 inch (1TB, WiFi+Cellular)"),
    ],
    "iPad_pro_12_9_3rd_gen": [
        ("iPad8,5", "iPad Pro 12.9 inch 3rd Gen (WiFi)"),
        ("iPad8,6", "iPad Pro 12.9 inch 3rd Gen (1TB, WiFi)"),
        ("iPad8,7", "iPad Pro 12.9 inch 3rd Gen (WiFi+Cellular)"),
        ("iPad8,8", "iPad Pro 12.9 inch 3rd Gen (1TB, WiFi+Cellular)"),
    ],
    "iPad_pro_11_2nd_gen": [
        ("iPad8,9", "iPad Pro 11 inch 2nd Gen (WiFi)"),
        ("iPad8,10", "iPad Pro 11 inch 2nd Gen (WiFi+Cellular)"),
    ],
    "iPad_pro_12_9_4th_gen": [
        ("iPad8,11", "iPad Pro 12.9 inch 4th Gen (WiFi)"),
        ("iPad8,12", "iPad Pro 12.9 inch 4th Gen (WiFi+Cellular)"),
    ],
    "iPad_mini_5th_gen": [
        ("iPad11,1", "iPad mini 5th Gen (WiFi)"),
        ("iPad11,2", "iPad mini 5th Gen"),
    ],
    "iPad_air_3rd_gen": [
        ("iPad11,3", "iPad Air 3rd Gen (WiFi)"),
        ("iPad11,4", "iPad Air 3rd Gen"),
    ],
}


def create_device_lists(devices_list):
    device_list = []
    name_list = []
    for device in devices_list:
        device_list.append(device[0])
        name_list.append(device[1])
    return (device_list, name_list)


def create_payload(device_list):
    payload = []
    for i in device_list:
        payload.extend(i)
    return payload


def show_iphones():
    for k, _ in iPhones.items():
        print(k)


def show_ipads():
    for k, _ in iPads.items():
        print(k)
