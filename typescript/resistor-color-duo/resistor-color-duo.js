//1. map [String] -> [Number]
//2. join [Number] -> String
//3.slice String -> String
//4. parse String -> Number
//Value :: [String] -> Number
export const value = colorValues => {
    return colorValues.map(colorValue => COLORS.indexOf(colorValue));
};
export const COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
];
//# sourceMappingURL=resistor-color-duo.js.map