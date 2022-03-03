import React, {useEffect, useState} from 'react';
import { KeyboardAvoidingView, StyleSheet, Text, View, TextInput, TouchableOpacity, Keyboard, ScrollView } from 'react-native';
import BackButton from '../components/BackButton';
import BackContainer from '../components/BackContainer';
import Header from '../components/Header';
import CheckTask from '../components/CheckTask';
import LoginScreen from './LoginScreen';
const STORAGE_KEY = '@save_email';

export default function CheckList({navigation}) {
  const [email, setEmail] = useState();
  const [task, setTask] = useState();
  const [taskItems, setTaskItems] = useState([]);

  const handleAddTask = () => {
    Keyboard.dismiss();
    setTaskItems([...taskItems, task])
    setTask(null);

    let url;
    url = `https://b9df-120-57-213-54.ngrok.io/patient/checklist`;
    fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        Text: task,
        Function: 'Add',
        returnSecureToken: true,
      }),
    })
      .then((res) => {
        if (res) {
          return res.data;
        } else {
          return res.json().then((data) => {
            let errorMessage = 'Task not stored';
            throw new Error(errorMessage);
          });
        }
      })
      .catch((error) => {
        console.error(error);
        setTask('');
        setTaskItems('');
      });

  }

  const readData = async () => {
    try {
      const userEmail = await AsyncStorage.getItem(STORAGE_KEY)

      if (userEmail !== null) {
        setEmail(userEmail)
      }
    } catch (e) {
      alert('Failed to fetch the email from storage')
    }
  }

  useEffect(() => {
  readData()
  }, [])

  const completeTask = (index) => {
    let itemsCopy = [...taskItems];
    itemsCopy.splice(index, 1);
    setTaskItems(itemsCopy)
    let url;
    url = `https://b9df-120-57-213-54.ngrok.io/patient/checklist`;
    fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        Text: taskItems,
        Function: 'Remove',
        returnSecureToken: true,
      }),
    })
      .then((res) => {
        if (res) {
          return res.data;
        } else {
          return res.json().then((data) => {
            let errorMessage = 'Task not stored';
            throw new Error(errorMessage);
          });
        }
      })
      .catch((error) => {
        console.error(error);
        setTask('');
        setTaskItems('');
      });
  }

  return (
    <BackContainer>
      <BackButton goBack={navigation.goBack}/>
      <Header>Check List</Header>
    <View style={styles.container}>
      <ScrollView contentContainerStyle={{flexGrow: 1}}
        keyboardShouldPersistTaps='handled'>
      <View style={styles.tasksWrapper}>
        <View style={styles.items}>
          {taskItems.map((item, index) => {
              return (
                <TouchableOpacity key={index}  onPress={() => completeTask(index)}>
                  <CheckTask text={item} /> 
                </TouchableOpacity>
              )
            })
          }
        </View>
      </View>   
      </ScrollView>
    
      <KeyboardAvoidingView 
        behavior={Platform.OS === "ios" ? "padding" : "height" }
        style={styles.writeTaskWrapper}>
        <TextInput style={styles.input} placeholder={'Write a task'} value={task} onChangeText={text => setTask(text)} />
        <TouchableOpacity onPress={() => handleAddTask()}>
          <View style={styles.addWrapper}>
            <Text style={styles.addText}>+</Text>
          </View>
        </TouchableOpacity>
      </KeyboardAvoidingView>
      
    </View>
    </BackContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8fdff',
  },
  tasksWrapper: {
    paddingTop: 20,
    paddingHorizontal: 20,
  },
  sectionTitle: {
    marginLeft: 10,
    fontSize: 24,
    fontWeight: 'bold'
  },
  items: {
    marginTop: 30,
  },
  writeTaskWrapper: {
    position: "relative",
    bottom: 10,
    width: '100%',
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center'
  },
  input: {
    paddingVertical: 15,
    paddingHorizontal: 15,
    backgroundColor: '#FFF',
    borderRadius: 60,
    borderColor: '#C0C0C0',
    borderWidth: 1,
    width: 250,
  },
  addWrapper: {
    width: 60,
    height: 60,
    backgroundColor: '#FFF',
    borderRadius: 60,
    justifyContent: 'center',
    alignItems: 'center',
    borderColor: '#C0C0C0',
    borderWidth: 1,
  },
  addText: {},
});