import {
	FormControl,
	FormLabel,
	FormErrorMessage,
	FormHelperText,
	Input,
	Button,
	Stack,
	Text
} from "@chakra-ui/react";
import React, { useState } from 'react';


export default function MyForm(props) {
	const [roomCode, setRoomCode] = useState("");
	const [name, setName] = useState("");

	const handleSubmit = async function(event) {
		event.preventDefault();
		// const res = await fetch("http://localhost:4000/join-room/" + roomCode, {
		// 	method: 'POST',
		// 	headers: {
		// 		'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify({ name })
		// })
		const path = "/" + roomCode + "/waiting"; 
		props.history.push(path);
	}

	return (
		<Stack maxWidth={500} margin="auto" marginTop={20} spacing={5}>
			<Text fontSize="4xl">Likes and Dislikes</Text>
			
			<form onSubmit={handleSubmit}>
				<Stack spacing={5}>
					<FormControl>
						<FormLabel htmlFor="room-code">Room code</FormLabel>
						<Input
							type="text"
							id="roomCode"
							isRequired
							onChange={({ target }) => setRoomCode(target.value)}
						/>
						<FormLabel htmlFor="name">Name</FormLabel>
						<Input
							type="text"
							id="name"
							isRequired
							onChange={({ target }) => setName(target.value)}
						/>
						<FormHelperText htmlFor="name">
							Please use your real name to avoid enraging certain people.
						</FormHelperText>
					</FormControl>
					<FormControl>
						<Button type="submit">
							Enter
						</Button>
					</FormControl>
				</Stack>
			</form>
			</Stack>
			)
}