#ex43
class Scene(object):
    
        def enter(self):
            pass
            

        def play(self):
            pass
            
class Engine(object):
    
       def _init_(self, scene_map):
           pass   
            
class Death(Scene):
    
    def enter(self):
        pass
        
class CentralCorridor(Scene):
    
    def enter(self):
        pass
        
class LaserWeaponArmory(Scene):
    
    def enter(self):
        pass

class TheBridge(Scene):
    
    def enter(self):
        pass
        
class EscapePod(Scene):
    
    def enter(self):
        pass
        
class Map(object):
    
    def _init_(self, start_scene):
        pass
    
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        

a_map = Map('centra_corridor')
a_game = Engine(a_map)
a_game.play()