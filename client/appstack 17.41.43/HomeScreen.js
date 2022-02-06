import React, {useState} from "react";
import { useNavigation } from "@react-navigation/native"
import { StyleSheet, View, Text, Alert, Button } from "react-native";
import { Input } from 'react-native-elements';

export default function HomeScreen() {
    const navigation = useNavigation();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const login = () =>{
        if(email === "user@gmail.com" && password === "pass") {
             navigation.navigate('ProductScreen');
        } else {
             Alert.alert("Error","Login Info Incorrect");
         }
    };

    return (
        <View style={styles.container}>
            <Input 
                placeholder="Email" 
                onChangeText={(text) => setEmail(text)}
                value={email}
            />
            <Input 
                placeholder="Password" 
                onChangeText={(text) => setPassword(text)}
                value={password}
                secureTextEntry
            />
             <Button title="Login" onPress={login}/> 
        </View>
    );
}

const styles = StyleSheet.create({
  container:{
    flex:1,
    marginTop:20,
    backgroundColor:"#ebf0f7"
  }
}
);
