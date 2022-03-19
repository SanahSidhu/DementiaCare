import React, { Component } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import BackContainer from '../components/BackContainer';
import BackButton from '../components/BackButton';
import Header from '../components/Header';
import { useNavigation } from '@react-navigation/native';
import { theme } from '../core/theme'
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Image,
  Alert,
  ScrollView,
  FlatList,
  Button
} from 'react-native';

export default class PhotoScreen extends Component {
<<<<<<< Updated upstream

=======
  // const [email, setEmail] = useState();
  // const [isLoading, setLoading] = useState(true);
  // const baseUrl = 'https://8503-122-174-132-140.ngrok.io';
  // const [data, setData] = useState([]);
  // console.log(data);

// const readData = async () => {
//     try {
//       const userEmail = await AsyncStorage.getItem(STORAGE_KEY)
//       if (userEmail !== null) {
//         alert('email fetched')
//         setEmail(userEmail)
//       }
//     } catch (e) {
//       alert('Failed to fetch the data from storage')
//     }
//   }

//   useEffect(() => {
//     readData()
//   }, [])

// useEffect(() => {
//     let url;
//     url = `${baseUrl}/patient/photos?Email=${email}`;
//   alert('Get Request Sent')
//   fetch(url)
//       .then((response) => response.json())
//       .then((json) => setData(json))
//       .catch((error) => console.error(error))
//       .finally(() => setLoading(false));
//   }, []);

//   const handleAddTask = () => {
//     Keyboard.dismiss();
//     setTaskItems([...taskItems, task])
//     setTask(null);

//     let url;
//     url = `${baseUrl}/patient/photos`;


//     fetch(url, {
//       method: 'POST',
//       headers: {
//         Accept: 'application/json',
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({
//         Email: email,
//         Text: task,
//         Function: 'Add',
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

//   }
>>>>>>> Stashed changes

  constructor(props) {
    super(props);
    this.state = {
      data: [
        {id:1, title: "After Marriage",                  time:"1974-08-01", image:"https://daily.jstor.org/wp-content/uploads/2016/08/wedding_party_1050x700.jpg", description:"The person sitting on the right of the chair is you, and right is John(Husband). Left corner on photo is Mary (John's Sister). Next to you is your sister (Beth)."},
        {id:2, title: "Your House",             time:"2018-03-25 12:00 pm", image:"https://www.mydomaine.com/thmb/L2QLQb1AoAkpuTqmyZmVnpeDEoc=/2121x1193/smart/filters:no_upscale()/GettyImages-469432252-3a4c307c981244e186f129f24cc8c89f.jpg"} ,
        {id:3, title: "Dipiscing elit. Aenean ",            time:"2017-08-05 12:21 pm", image:"https://via.placeholder.com/400x200/000080/000000", description:"Lorem ipsum dolor sit , consectetuer  elit. Aenean commodo ligula..."}, 
        {id:4, title: "Commodo ligula eget dolor.",         time:"2015-08-12 12:00 pm", image:"https://via.placeholder.com/400x200/48D1CC/000000", description:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula..."}, 
        {id:5, title: "Aenean massa. Cum sociis",           time:"2013-06-12 12:11 pm", image:"https://via.placeholder.com/400x200/9370DB/000000", description:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  commodo ligula..."}, 
        {id:6, title: "Natoque penatibus et magnis",        time:"2018-08-12 12:56 pm", image:"https://via.placeholder.com/400x200/DA70D6/000000", description:"Lorem ipsum  sit amet, consectetuer adipiscing elit. Aenean commodo ligula..."}, 
        {id:7, title: "Dis parturient montes, nascetur",    time:"2018-08-12 12:33 pm", image:"https://via.placeholder.com/400x200/DDA0DD/000000", description:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula..."}, 
        {id:8, title: "Ridiculus mus. Donec quam",          time:"2018-06-12 12:44 pm", image:"https://via.placeholder.com/400x200/4169E1/000000", description:"Lorem ipsum  sit amet, consectetuer adipiscing elit.  commodo ligula..."},
        {id:9, title: "Felis, ultricies nec, pellentesque", time:"2012-07-12 12:23 pm", image:"https://via.placeholder.com/400x200/FA8072/000000", description:"Lorem ipsum dolor sit amet, consectetuer  elit. Aenean commodo ligula..."},
      ]
    };
  }

  

  render() {
    const { navigate } = this.props.navigation;    
    return (
      <BackContainer>
      <BackButton goBack={this.props.navigation.goBack}/>
      <Header> PhotoScreen </Header>
      <View style={styles.container}>
        <FlatList style={styles.list}
          data={this.state.data}
          keyExtractor= {(item) => {
            return item.id;
          }}
          ItemSeparatorComponent={() => {
            return (
              <View style={styles.separator}/>
            )
          }}
          renderItem={(post) => {
            const item = post.item;
            return (
              <View style={styles.card}>
                <Image style={styles.cardImage} source={{uri:item.image}}/>
                <View style={styles.cardHeader}>
                  <View>
                    <Text style={styles.title}>{item.title}</Text>
                    <Text style={styles.description}>{item.description}</Text>
                    <View style={styles.timeContainer}>
                      <Image style={styles.iconData} source={{uri: 'https://img.icons8.com/color/96/3498db/calendar.png'}}/>
                      <Text style={styles.time}>{item.time}</Text>
                    </View>
                  </View>
                </View>
              </View>
            )
          }}/>
      </View>
      </BackContainer>
    );
  }
}

const styles = StyleSheet.create({
  container:{
    paddingRight: 20,
    flex:1,
    marginTop:20,
  },
  list: {
    paddingHorizontal: 17,
    backgroundColor:theme.colors.surface,
  },
  separator: {
    marginTop: 10,
  },
  /******** card **************/
  card:{
    shadowColor: '#00000021',
    shadowOffset: {
      width: 2
    },
    shadowOpacity: 0.5,
    shadowRadius: 4,
    marginVertical: 8,
    backgroundColor:"white"
  },
  cardHeader: {
    paddingVertical: 17,
    paddingHorizontal: 16,
    borderTopLeftRadius: 1,
    borderTopRightRadius: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  cardContent: {
    paddingVertical: 12.5,
    paddingHorizontal: 16,
  },
  cardFooter:{
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingTop: 12.5,
    paddingBottom: 25,
    paddingHorizontal: 16,
    borderBottomLeftRadius: 1,
    borderBottomRightRadius: 1,
    backgroundColor:"#EEEEEE",
  },
  cardImage:{
    flex: 1,
    height: 150,
    width: null,
  },
  /******** card components **************/
  title:{
    fontSize:18,
    flex:1,
  }, 
  description:{
    fontSize:15,
    color:"#888",
    flex:1,
    marginTop:5,
    marginBottom:5,
  },
  time:{
    fontSize:13,
    color: "#808080",
    marginTop: 5
  },
  icon: {
    width:25,
    height:25,
  },
  iconData:{
    width:15,
    height:15,
    marginTop:5,
    marginRight:5
  },
  timeContainer:{
    flexDirection:'row'
  },
});  
                                            