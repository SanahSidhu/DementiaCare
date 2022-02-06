import React, { useEffect, useState} from "react";
import { Alert, SafeAreaView, Text, View } from 'react-native';
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import HomeScreen from "./HomeScreen";
import ProductScreen from './ProductScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        {/* <Stack.Screen name="Home" component={HomeScreen} /> */}
        <Stack.Screen name="DementiaCare" component={ProductScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}


