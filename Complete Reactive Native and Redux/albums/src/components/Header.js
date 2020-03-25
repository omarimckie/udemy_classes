//this file is to create the header that will be a rectangle box with the words "Albums"

//Import a library to help create a component
import React from 'react';
import { Text, View } from 'react-native';

//Create a component
const Header = (props) => {             //props is a javascript object
    const { textStyle, viewStyle } = styles;

    return (
        <View style={viewStyle}>
            <Text style={textStyle}>{props.headerText}</Text>   
        </View>
    )
};

const styles = {
    viewStyle: {
        backgroundColor: '#F8F8F8',
        alignItems: 'center',
        justifyContent: 'center', 
        height: 60,
        paddingTop: 15,
        shadowColor:'#000',
        shadowOffset: {height:2,width:0},
        shadowOpacity: .2, 
        elevation:8,
        position:'relative'
    },

    textStyle: {
        fontSize: 20
    }    
};

//Make the component available for other parts of the app
export default Header;