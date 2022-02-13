import React from 'react'
import Background from '../components/Background'
import Logo from '../components/Logo'
import Header from '../components/Header'
import Paragraph from '../components/Paragraph'
import Button from '../components/Button'

export default function Settings({ navigation }) {
  return (
    <Background>
      <Logo />
      <Header>Settings</Header>
      <Button
        mode="outlined"
        onPress={() =>
          navigation.navigate('')}
      >
        Logout
      </Button>
    </Background>
  )
}