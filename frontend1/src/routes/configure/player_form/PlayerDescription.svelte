<script>
    import Age from './Age.svelte';
	import Energy from './Energy.svelte'
	import Role from './Role.svelte';
	import Humor from './Humor.svelte';
	import Aptitude from './Aptitude.svelte';
    import HairColor from './HairColor.svelte';

    export let player_info={
        age:1,
        hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    }
    
</script>
<div>
    <p>
        How old are your player?
    </p>
    <div class=button-container>
        <Age bind:age={player_info.age}/>
    </div>
    <p>
        Hair color
    </p>
    <div class=button-container>
        <HairColor bind:selected={player_info.hair_color}/>
    </div>
    <p>
        Choose the communication type of your player
    </p>
    <div class=button-container>
        <Energy bind:selected={player_info.energy}/>
    </div>
    
    <p>
        How do you define your player?
    </p>
    <div class=button-container>
        <Role bind:selected={player_info.role}/>	
        
    </div>
    <p>
        Choose your player's sense of humor
    </p>
    <div class=button-container>
        <Humor bind:selected={player_info.humor}/>
    </div>

    <p>
        Choose the main skill or ability
    </p>
    <div class=button-container>
        <Aptitude bind:selected={player_info.aptitude}/>

    </div>
    

</div>

<style>
	.button-container {
	  display: flex;
      flex-direction: column;
	  justify-content: center;
	}
	/* p {
		color: rgb(47, 47, 47);
    	font-weight:lighter;
   	 	text-align: center;
		font-size: 30px;
    	font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		width: 100%;
	} */
    
</style>
