import React, { useCallback, useEffect, useState } from "react";
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Alert, Linking, Platform, View, StyleSheet, TouchableOpacity } from "react-native";
import Icon from 'react-native-vector-icons/MaterialIcons';
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Header from '../components/Header'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import { relationValidator } from '../helpers/relationValidator'
import { nameValidator } from '../helpers/nameValidator'
import { phonenoValidator } from '../helpers/phonenoValidator';

export default function EmergencyForm({ navigation }) {
  const [email, setEmail] = useState();
  const [isLoading, setLoading] = useState(true);
  const [name, setName] = useState({ value: '', error: '' })
  const [relation, setRelation] = useState({ value: '', error: '' })
  const [phoneno, setPhoneno] = useState({ value: '', error: '' })
  const baseUrl = 'https://8503-122-174-132-140.ngrok.io';

  const [data, setData] = useState([]);
  console.log(data);

  const readData = async () => {
    try {
      const userEmail = await AsyncStorage.getItem(STORAGE_KEY)
      if (userEmail !== null) {
        alert('email fetched')
        setEmail(userEmail)
      }
    } catch (e) {
      alert('Failed to fetch the data from storage')
    }
  }

  useEffect(() => {
    readData()
  }, [])

  useEffect(() => {
    let url;
    url = `${baseUrl}/patient/emergencycontacts?Email=${email}`;
  alert('Get Request Sent')
  fetch(url)
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error(error))
      .finally(() => setLoading(false));
  }, []);

  const onSignUpPressed = () => {
    const nameError = nameValidator(name.value)
    const relationError = relationValidator(relation.value)
    const phonenoError = phonenoValidator(phoneno.value)
    if (relationError || nameError ) {
      setName({ ...name, error: nameError })
      setRelation({ ...relation, error: relationError })
      setPhoneno({ ...phoneno, error: phonenoError })
      return
    }

    const number = "+819060138751";
    Linking.openURL(`tel:${number}`)

    // Linking.openURL(`tel:${JSON.stringify(phoneno.value)}`)

    let url;
    url = `${baseUrl}/patient/emergencycontacts`;
    fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        Email: email,
        Name: name,
        Relation: relation,
        PhoneNumber: phoneno,
        Function: 'Add',
        returnSecureToken: true,
      }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          return res.json().then((data) => {
            let errorMessage = 'Authentication failed!';
            throw new Error(errorMessage);
          });
        }
      })
      .catch((error) => {
        console.error(error);
        setName('');
        setPhoneno('');
        setRelation('');
      });
  }

  return (
    <Background>
      <BackButton goBack={navigation.goBack} />
      <Header> Emergency Contact</Header>
      <TextInput
        label="Name"
        returnKeyType="next"
        value={name.value}
        onChangeText={(text) => setName({ value: text, error: '' })}
        error={!!name.error}
        errorText={name.error}
      />
      <TextInput
        label="Relation"
        returnKeyType="Relation"
        value={relation.value}
        onChangeText={(text) => setRelation({ value: text, error: '' })}
        error={!!relation.error}
        errorText={relation.error}
      />
      <TextInput
        label="Emergency Contact"
        returnKeyType="next"
        value={phoneno.value}
        onChangeText={(text) => setPhoneno({ value: text, error: '' })}
        error={!!phoneno.error}
        errorText={phoneno.error}
      />
      <Button
        mode="contained"
        value={phoneno.value}
        onPress={onSignUpPressed}
        style={{ marginTop: 24 }}
      >
        Call
      </Button>
      
    </Background>
  )
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    marginTop: 4,
  },
  link: {
    fontWeight: 'bold',
    color: theme.colors.primary,
  },
})


// const EmergencyCall = () => {

//     const number = "+918147742334";

//     let url;
//     url = `https://d2a4-120-57-216-248.ngrok.io/patient/login`;
//     fetch(url, {
//       method: 'POST',
//       headers: {
//         Accept: 'application/json',
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({
//         Emergency: number,
//         returnSecureToken: true,
//       }),
//     })
//       .then((res) => {
//         if (res) {
//           return res.data;
//         } else {
//           return res.json().then((data) => {
//             let errorMessage = 'Task not stored';
//             throw new Error(errorMessage);
//           });
//         }
//       })
//       .catch((error) => {
//         console.error(error);
//         setTask('');
//         setTaskItems('');
//       });

//     return (
//         <View style={styles.container}>   
//             <View style={styles.buttonContainer}>
//                 <Icon name="call" size={50} color="#900" onPress={() => {
//                     Linking.openURL(`tel:${number}`)
//                 }} color="#3399ff" ></Icon>
//             </View>
           
//         </View>
//     );
// };

// const styles = StyleSheet.create({
//     container: {
//         flex:1,
//         marginTop:20,
//         padding:20,
//         backgroundColor:"#ebf0f7",
//         justifyContent: "center", 
//         alignItems: "center", 
//         height:"50%", 
//         width:'70%', 
//         borderRadius:40, 
//         margin:'auto', 
//         textAlign:'center' 
//     },
//     buttonContainer: {
//         margin: 10
//     }
// });

// export default EmergencyCall