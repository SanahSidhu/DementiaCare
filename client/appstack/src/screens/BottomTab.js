import { StyleSheet, Text, View } from 'react-native';
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Settings from './Settings';
import Dashboard from './Dashboard';
import LoginScreen from './LoginScreen';
import CheckList from './CheckList';

const Tab = createBottomTabNavigator();

const BottomTab = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Dashboard" component={Dashboard} />
      <Tab.Screen name="Settings" component={Settings} />
      {/* <Tab.Screen name="CheckList" component={CheckList} /> */}
    </Tab.Navigator>
  );
};

export default BottomTab;


