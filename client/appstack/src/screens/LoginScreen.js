import React, { useEffect, useState } from 'react'
import AsyncStorage from '@react-native-async-storage/async-storage';
import { TouchableOpacity, StyleSheet, View } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Logo from '../components/Logo'
import Header from '../components/Header'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import { emailValidator } from '../helpers/emailValidator'
import { passwordValidator } from '../helpers/passwordValidator'
import axios from "axios";
const STORAGE_KEY = '@save_email';

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState()
  const [password, setPassword] = useState({ value: '', error: '' })
  const [isLoading, setIsLoading] = useState(false);
<<<<<<< Updated upstream
  const baseUrl = ' ';
=======
  const baseUrl = 'https://8503-122-174-132-140.ngrok.io';
>>>>>>> Stashed changes

  const onLoginPressed = async (event) => {
    const passwordError = passwordValidator(password.value)
    if (passwordError) {
      setPassword({ ...password, error: passwordError })
      return
    }
<<<<<<< Updated upstream
    setIsLoading(true);
    try {
      const response = await axios.post(`${baseUrl}/patient/login`, {
        email,
        password,
      });
      if (response.status === 201) {
        alert(` You have created: ${JSON.stringify(response.data)}`);
        setIsLoading(false);
=======
  //   setIsLoading(true);
  //   try {
  //     const response = await axios.post(`${baseUrl}/patient/login`, {
  //       email,
  //       password,
  //     });
  //     if (response.status === 201) {
  //       alert(` You have created: ${JSON.stringify(response.data)}`);
  //       setIsLoading(false);
  //       setEmail('');
  //       setPassword('');
  //     } else {
  //       throw new Error("An error has occurred");
  //     }
  //   } catch (error) {
  //     alert("An error has occurred");
  //     setIsLoading(false);
  //   }

    let url;
    url = `https://8503-122-174-132-140.ngrok.io/patient/login`;
    fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        Email: email,
        Password: password,
        returnSecureToken: true,
      }),
    })
      .then((res) => {
        if (res) {
          return res.data;
        } else {
          return res.json().then((data) => {
            let errorMessage = 'Authentication failed!';
            throw new Error(errorMessage);
          });
        }
      })
      .catch((error) => {
        console.error(error);
>>>>>>> Stashed changes
        setEmail('');
        setPassword('');
      } else {
        throw new Error("An error has occurred");
      }
    } catch (error) {
      alert("An error has occurred");
      setIsLoading(false);
    }

    // let url;
    // url = `https://b9df-120-57-213-54.ngrok.io/patient/login`;
    // fetch(url, {
    //   method: 'POST',
    //   headers: {
    //     Accept: 'application/json',
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({
    //     Email: email,
    //     Password: password,
    //     returnSecureToken: true,
    //   }),
    // })
    //   .then((res) => {
    //     if (res) {
    //       return res.data;
    //     } else {
    //       return res.json().then((data) => {
    //         let errorMessage = 'Authentication failed!';
    //         throw new Error(errorMessage);
    //       });
    //     }
    //   })
    //   .catch((error) => {
    //     console.error(error);
    //     setEmail('');
    //     setPassword('');
    //   });

      navigation.navigate('MainScreen');
  }

  const saveData = async () => {
    
    try {
      await AsyncStorage.setItem(STORAGE_KEY, email)
      alert('Email successfully saved')
    } catch (e) {
      alert('Failed to save the data to the storage')
    }
  }

    const readData = async () => {
    try {
      const userEmail = await AsyncStorage.getItem(STORAGE_KEY)

      if (userEmail !== null) {
        setEmail(userEmail)
      }
    } catch (e) {
      alert('Failed to fetch the data from storage')
    }
  }

  useEffect(() => {
    readData()
  }, [])

  const onChangeText = userEmail => setEmail(userEmail)

  const onSubmitEditing = () => {
    if (!email) return

    saveData(email)
    setEmail('')
  }

  return (
    <Background>
      <BackButton goBack={navigation.goBack} />
      <Logo />
      <Header>Welcome back.</Header>
      <TextInput
        label="Email"
        returnKeyType="next"
        onChangeText={onChangeText}
        onSubmitEditing={onSubmitEditing}
        autoCapitalize="none"
        autoCompleteType="email"
        textContentType="emailAddress"
        keyboardType="email-address"
      />
      <TextInput
        label="Password"
        returnKeyType="done"
        value={password.value}
        onChangeText={(text) => setPassword({ value: text, error: '' })}
        error={!!password.error}
        errorText={password.error}
        secureTextEntry
      />
      <View style={styles.forgotPassword}>
        <TouchableOpacity
          onPress={() => navigation.navigate('ResetPasswordScreen')}>
          <Text style={styles.forgot}>Forgot your password?</Text>
        </TouchableOpacity>
      </View>
      <Button mode="contained" onPress={onLoginPressed}>
        Login
      </Button>
      <View style={styles.row}>
        <Text>Don’t have an account? </Text>
        <TouchableOpacity onPress={() => navigation.replace('RegisterScreen')}>
          <Text style={styles.link}>Sign up</Text>
        </TouchableOpacity>
      </View>
    </Background>
  )
}

const styles = StyleSheet.create({
  forgotPassword: {
    width: '100%',
    alignItems: 'flex-end',
    marginBottom: 24,
  },
  row: {
    flexDirection: 'row',
    marginTop: 4,
  },
  forgot: {
    fontSize: 13,
    color: theme.colors.secondary,
  },
  link: {
    fontWeight: 'bold',
    color: theme.colors.primary,
  },
})
