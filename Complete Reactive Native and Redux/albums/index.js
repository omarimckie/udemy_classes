//Import a library to help create a component
import React from 'react';
import { Text, AppRegistry } from 'react-native';
import Header from './src/components/Header';
import AlbumList from './src/components/AlbumList';

//Create a component
const App = () => {         //App is the component
    return (
        <Header headerText = {'Albums'}/>   //headerText is the name of the prop being passed
    );
};

//Render it to the device
AppRegistry.registerComponent('albums', () => App);