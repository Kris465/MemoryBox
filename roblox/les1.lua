local part = script.Parent
part.Shape = Enum.PartType.Ball
part.Material = Enum.Material.Neon

-- Ждём 0.1 сек, чтобы Touched не сработал сразу
task.wait(0.1)  

local function onTouch(otherPart)  
	local player = game.Players:GetPlayerFromCharacter(otherPart.Parent)  
	if player then  
		part:Destroy()  
	end  
end  

part.Touched:Connect(onTouch)