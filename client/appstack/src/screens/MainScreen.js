import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import BottomTab from './BottomTab';
import UserScreen from './UserScreen';
import Settings from './Settings';
import CheckList from './CheckList';
import PhotoScreen from './PhotoScreen';
import NoteScreen from './NoteScreen';
import MemoScreen from './MemoScreen';
import Contacts from './Contacts';

const Stack = createStackNavigator()

export default function MainScreen() {
  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator screenOptions={{headerShown: false,}}>
        <Stack.Screen name="BottomTab" component={BottomTab} />
        <Stack.Screen name="UserScreen" component={UserScreen} />
         <Stack.Screen name="CheckList" component={CheckList} />
         <Stack.Screen name="PhotoScreen" component={PhotoScreen} />
         <Stack.Screen name ="MemoScreen" component={MemoScreen} />
         <Stack.Screen name ="NoteScreen" component={NoteScreen} />
         <Stack.Screen name="Contacts" component={Contacts}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: "center",
    justifyContent: "center",
  },
});