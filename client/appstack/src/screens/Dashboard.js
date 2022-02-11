import React, { Component } from 'react';
import Background from '../components/Background'
import Logo from '../components/Logo'
import Button from '../components/Button'
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableOpacity,
  FlatList,
  Dimensions,
  Alert,
  ScrollView
} from 'react-native';

export default class Dashboard extends Component{

  constructor(props) {
    super(props);
    this.state = {
      modalVisible:false,
      userSelected:[],
      data: [
        {id:1,  name: "Calendar", image:"https://img.icons8.com/external-xnimrodx-lineal-color-xnimrodx/344/external-schedule-calendar-xnimrodx-lineal-color-xnimrodx.png"},
        {id:2,  name: "Medication",   image:"https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-medicine-hospital-justicon-lineal-color-justicon.png"},
        {id:6,  name: "Photos",   image:"https://img.icons8.com/external-vitaliy-gorbachev-lineal-color-vitaly-gorbachev/344/external-photos-photography-vitaliy-gorbachev-lineal-color-vitaly-gorbachev.png"} ,
        {id:5,  name: "Notes",   image:"https://img.icons8.com/external-bearicons-outline-color-bearicons/344/external-notes-graphic-design-bearicons-outline-color-bearicons.png"} ,
        {id:3,  name: "CheckList",       image:"https://img.icons8.com/external-vitaliy-gorbachev-lineal-color-vitaly-gorbachev/344/external-check-list-home-office-vitaliy-gorbachev-lineal-color-vitaly-gorbachev.png"} ,
        {id:4,  name: "Contacts",  component:"CheckList", image:"https://img.icons8.com/external-soft-fill-juicy-fish/344/external-contacts-folders-soft-fill-soft-fill-juicy-fish.png"} ,
      ]
    };
  }


  clickEventListener = (item) => {
    const { navigate } = this.props.navigation;
    if(item.name === "CheckList") {
        navigate('CheckList');
    } else if(item.name === "Photos") {
        navigate('PhotoScreen');
    } else if(item.name === "Notes") {
        navigate('MemoScreen');
    } else {
        Alert.alert('Message', 'Item clicked. '+item.name);
    }
  }

  render() {
    return (
      <View style={styles.container}>
        <FlatList 
          style={styles.contentList}
          columnWrapperStyle={styles.listContainer}
          data={this.state.data}
          keyExtractor= {(item) => {
            return item.id;
          }}
          renderItem={({item}) => {
          return (
            <TouchableOpacity style={styles.card} onPress={() => {this.clickEventListener(item)}}>
              <Image style={styles.image} source={{uri: item.image}}/>
              <View style={styles.cardContent}>
                <Text style={styles.name}>{item.name}</Text>
                <TouchableOpacity style={styles.followButton} onPress={()=> this.clickEventListener(item)}>
                  <Text style={styles.followButtonText}>Explore now</Text>  
                </TouchableOpacity>
              </View>
            </TouchableOpacity>
          )}}/>
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container:{
    flex:1,
    backgroundColor:"#f8fdff"
  },
  contentList:{
    flex:1,
  },
  cardContent: {
    marginLeft:20,
    marginTop:10
  },
  image:{
    width: 70,
    height:70,
    margin: 10,
  },

  card:{
    shadowColor: '#00000021',
    shadowOffset: {
      width: 0,
      height: 6,
    },
    shadowOpacity: 0.37,
    shadowRadius: 7.49,
    elevation: 12,

    marginLeft: 20,
    marginRight: 20,
    marginTop:20,
    backgroundColor:"white",
    padding: 10,
    flexDirection:'row',
    borderRadius:30,
  },

  name:{
    fontSize:18,
    flex:1,
    alignSelf:'center',
    color:"#3399ff",
    fontWeight:'bold'
  },
  followButton: {
    marginTop:10,
    height:35,
    width:100,
    padding:10,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius:30,
    backgroundColor: "white",
    borderWidth:1,
    borderColor:"#dcdcdc",
  },
  followButtonText:{
    color: "#dcdcdc",
    fontSize:12,
  },
});


 
