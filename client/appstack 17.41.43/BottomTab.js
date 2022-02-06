import { StyleSheet, Text, View } from 'react-native';
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import UserScreen from './UserScreen';
// import ProductScreen from './ProductScreen';
import CheckList from './CheckList';
import Dashboard from './Dashboard';
// import LoginScreen from './LoginScreen';

const Tab = createBottomTabNavigator();

const BottomTab = () => {
  return (
    <Tab.Navigator>
      {/* <Tab.Screen name="Login" component={LoginScreen} /> */}
      <Tab.Screen name="Dashboard" component={Dashboard} />
      <Tab.Screen name="User" component={UserScreen} />
      <Tab.Screen name="CheckList" component={CheckList} />
    </Tab.Navigator>
  );
};

export default BottomTab;


