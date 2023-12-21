<script>
    import Age from './Age.svelte';
	import Energy from './Energy.svelte'
	import Role from './Role.svelte';
	import Humor from './Humor.svelte';
	import Aptitude from './Aptitude.svelte';
    import HairColor from './HairColor.svelte';

    export let player_info={
        player_id:"",
        age:1,
        hair_color:"",
        energy:"",
        role: "",
        aptitude:"",
        humor:""
    }
    
</script>
<div>
    <h2>
        How old are your player?
    </h2>
    <div class=button-container>
        <Age bind:age={player_info.age}/>
    </div>
    <h2>
        Hair color
    </h2>
    <div class=button-container>
        <HairColor bind:selected={player_info.hair_color}/>
    </div>
</div>
<div>
    <h2>
        Choose the communication type of your player
    </h2>
    <div class=button-container>
        <Energy bind:selected={player_info.energy}/>
    </div>
    

</div>
<div>
    <h2>
        How do you define your player?
    </h2>
    <div class=button-container>
        <Role bind:selected={player_info.role}/>	
        
    </div>
    

</div>
<div>
    <h2>
        Choose your player's sense of humor
    </h2>
    <div class=button-container>
        <Humor bind:selected={player_info.humor}/>
    </div>

</div>
<div>
    <h2>
        Choose the main skill or ability
    </h2>
    <div class=button-container>
        <Aptitude bind:selected={player_info.aptitude}/>

    </div>
    

</div>
<style>
	.button-container {
	  display: flex;
	  justify-content: center;
	}
	h2 {
		color: rgb(47, 47, 47);
    	font-weight:lighter;
   	 	text-align: center;
		font-size: 30px;
    	font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		width: 100%;
	}
    
</style>
