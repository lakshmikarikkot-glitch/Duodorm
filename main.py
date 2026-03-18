import React, { useState } from 'react';
import { View, Text, StyleSheet, Image, Dimensions, PanResponder, Animated } from 'react-native';

const { width, height } = Dimensions.get('window');

const SwipeScreen = () => {
  const [profiles, setProfiles] = useState([
    { id: 1, name: 'Ananya', major: 'ECE', vibe: 'Night Owl', tags: ['#Skincare', '#LoFi'], image: 'https://via.placeholder.com/400x600/121212/00d4ff' },
    { id: 2, name: 'Rohan', major: 'CS', vibe: 'Early Bird', tags: ['#Gaming', '#Gym'], image: 'https://via.placeholder.com/400x600/121212/ff007a' },
  ]);

  // High-contrast, glossy theme constants
  const COLORS = {
    background: '#0F0F0F',
    card: '#1A1A1A',
    accent: '#00D4FF', // Electric Cyan
    secondary: '#FF007A', // Neon Pink
    text: '#FFFFFF'
  };

  return (
    <View style={[styles.container, { backgroundColor: COLORS.background }]}>
      <Text style={styles.header}>DuoDorm</Text>
      
      {profiles.map((item, i) => (
        <View key={item.id} style={styles.cardContainer}>
           <View style={[styles.card, { backgroundColor: COLORS.card }]}>
              <Image source={{ uri: item.image }} style={styles.image} />
              <View style={styles.info}>
                <Text style={styles.name}>{item.name}, {item.major}</Text>
                <Text style={[styles.vibe, { color: COLORS.accent }]}>{item.vibe}</Text>
                <View style={styles.tagRow}>
                  {item.tags.map(tag => (
                    <Text key={tag} style={styles.tag}>{tag}</Text>
                  ))}
                </View>
              </View>
           </View>
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, paddingTop: 50, alignItems: 'center' },
  header: { fontSize: 28, fontWeight: 'bold', color: '#00D4FF', marginBottom: 20, letterSpacing: 2 },
  cardContainer: { position: 'absolute', top: 100 },
  card: {
    width: width * 0.9,
    height: height * 0.65,
    borderRadius: 25,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: '#333',
    elevation: 10,
  },
  image: { width: '100%', height: '75%', opacity: 0.8 },
  info: { padding: 20 },
  name: { fontSize: 24, fontWeight: 'bold', color: '#FFF' },
  vibe: { fontSize: 16, marginTop: 5, fontWeight: '600' },
  tagRow: { flexDirection: 'row', marginTop: 10 },
  tag: { color: '#AAA', marginRight: 10, fontSize: 12, fontStyle: 'italic' }
});

export default SwipeScreen