import React, { useCallback, useEffect, useState } from "react";
import { Alert, Button, Linking, Platform, StyleSheet, Text, View } from "react-native";
import Icon from 'react-native-vector-icons/MaterialIcons';


const LinkingPage = () => {

    const number = "+918147742334"

    return (
        <View style={styles.container}>   
            <View style={styles.buttonContainer}>
                <Icon name="call" size={50} color="#900" onPress={() => {
                    Linking.openURL(`tel:${number}`)
                }} color="#3399ff" ></Icon>
            </View>
           
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex:1,
        marginTop:20,
        padding:20,
        backgroundColor:"#ebf0f7",
        justifyContent: "center", 
        alignItems: "center", 
        height:"50%", 
        width:'70%', 
        borderRadius:40, 
        margin:'auto', 
        textAlign:'center' 
    },
    buttonContainer: {
        margin: 10
    }
});

export default LinkingPage