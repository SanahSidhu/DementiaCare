import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer} from "@react-navigation/native";
import BottomTab from './BottomTab';

export default function ProductScreen() {
  return (
    <NavigationContainer independent={true}>
      <BottomTab/>
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