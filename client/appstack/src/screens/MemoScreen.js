import AsyncStorage from '@react-native-async-storage/async-storage';
import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';

import NoteScreen from './NoteScreen';
import NoteDetail from '../components/NoteDetail';
import NoteProvider from '../contexts/NoteProvider';
import BackContainer from '../components/BackContainer';
import BackButton from '../components/BackButton';

const Stack = createStackNavigator();

export default function MemoScreen({navigation}) {

  return (
    <NavigationContainer independent={true}>
      <NoteProvider>
        <Stack.Navigator>
          <Stack.Screen component={NoteScreen} name='NoteScreen' />
          <Stack.Screen component={NoteDetail} name='NoteDetail' />
        </Stack.Navigator>
      </NoteProvider>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});