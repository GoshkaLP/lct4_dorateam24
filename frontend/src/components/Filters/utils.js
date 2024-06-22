
export const getOptionsAndMap = (data) => {
    const options = [];
    const map = new Map();
    data.data.forEach((item) => {
        options.push(item.title);
        map.set(item.title, item.title);
    });

    return { options, map }
}