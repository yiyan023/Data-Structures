var TimeLimitedCache = function() {
    this.hashmap = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existed = this.hashmap.has(key)
    
    if (existed) {
        clearInterval(this.hashmap.get(key).newTimeout)
    }

    const removeKey = () => {
        this.hashmap.delete(key)
    }

    const newTimeout = setTimeout(removeKey, duration)

    this.hashmap.set(key, { value, newTimeout })
    return existed
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.hashmap.has(key)) {
        return this.hashmap.get(key).value
    } else {
        return -1
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.hashmap.size
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
