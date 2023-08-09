import React, { useEffect, useState } from 'react';
import { Card, CardContent, Grid, Typography, makeStyles } from '@material-ui/core';
import axiosInstance from '../../axios';
import { useHistory } from 'react-router-dom';

const useStyles = makeStyles({
    hall: {
        textAlign: 'center',
        padding: '50px',
    },
    roomCard: {
        border: '1px solid #ccc',
        borderRadius: '10px',
        padding: '15px',
        margin: '10px',
        width: '250px',
        cursor: 'pointer',
        transition: 'background-color 0.3s, transform 0.2s',
        '&:hover': {
            backgroundColor: '#f5f5f5',
            transform: 'scale(1.02)',
        },
    },
    roomName: {
        fontSize: '20px',
        fontWeight: 'bold',
        marginBottom: '5px',
        color: '#2196f3',
    },
    roomDescription: {
        fontSize: '14px',
        color: '#666',
        marginBottom: '10px',
    },
    roomId: {
        fontSize: '14px',
        color: '#999',
    },
});

function ChatHall() {
    const classes = useStyles();
    const [rooms, setRooms] = useState([]);
    const history = useHistory();

    useEffect(() => {
        axiosInstance.get('chat/')
            .then(response => {
                const data = response.data;
                setRooms(data.rooms);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const handleCardClick = (slug) => {
        history.push(`/hall/${slug}`);
    };

    return (
        <div className={classes.hall}>
            <Typography variant="h4" color="primary" gutterBottom>
                Welcome to the Chat Hall
            </Typography>
            <Grid container spacing={3}>
                {rooms.map(room => (
                    <Grid item key={room.id} xs={12} sm={6} md={4}>
                        <Card className={classes.roomCard} onClick={() => handleCardClick(room.slug)}>
                            <CardContent>
                                <Typography className={classes.roomName}>{room.name}</Typography>
                                <Typography className={classes.roomDescription}>{room.description}</Typography>
                                <Typography className={classes.roomId}>Room ID: {room.id}</Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </div>
    );
}

export default ChatHall;